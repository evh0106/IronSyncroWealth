import { useQuery } from "@tanstack/react-query";
import type { Broker } from "@/shared/api/client";
import { apiClient } from "@/shared/api/client";
import { queryKeys } from "@/shared/lib/query-keys";
import type { MarketQuote } from "@/entities/market/model/types";

export function useMarketQuote(broker: Broker, symbol: string) {
  return useQuery({
    queryKey: queryKeys.market(broker, symbol),
    queryFn: async () => {
      const { data } = await apiClient(broker).get<MarketQuote>(`/api/v1/market/${symbol}`);
      return data;
    },
    staleTime: 2_000,
    refetchInterval: 3_000
  });
}