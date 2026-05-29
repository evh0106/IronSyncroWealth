import { useEffect } from "react";
import { useQueryClient } from "@tanstack/react-query";
import type { Broker } from "@/shared/api/client";
import { queryKeys } from "@/shared/lib/query-keys";

export function useRealtime(broker: Broker, symbol: string) {
  const queryClient = useQueryClient();

  useEffect(() => {
    const ws = new WebSocket(`ws://localhost:8000/ws/${broker}/${symbol}`);

    ws.onmessage = (event) => {
      try {
        const payload = JSON.parse(event.data) as { price?: number; volume?: number };
        queryClient.setQueryData(queryKeys.market(broker, symbol), (oldData: unknown) => {
          if (!oldData || typeof oldData !== "object") return oldData;
          return {
            ...(oldData as Record<string, unknown>),
            ...(payload.price !== undefined ? { price: payload.price } : {}),
            ...(payload.volume !== undefined ? { volume: payload.volume } : {})
          };
        });
      } catch {
        queryClient.invalidateQueries({ queryKey: queryKeys.market(broker, symbol) });
      }
    };

    return () => ws.close();
  }, [broker, symbol, queryClient]);
}