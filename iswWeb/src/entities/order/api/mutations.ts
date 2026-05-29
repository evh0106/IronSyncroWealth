import { useMutation, useQueryClient } from "@tanstack/react-query";
import type { Broker } from "@/shared/api/client";
import { apiClient } from "@/shared/api/client";
import { queryKeys } from "@/shared/lib/query-keys";
import type { OrderRequest, OrderResponse } from "@/entities/order/model/types";

export function useSubmitOrder(broker: Broker) {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (payload: OrderRequest) => {
      const { data } = await apiClient(broker).post<OrderResponse>("/api/v1/order", payload);
      return data;
    },
    onSuccess: (_result, variables) => {
      queryClient.invalidateQueries({ queryKey: queryKeys.orders(broker, variables.accountNo) });
      queryClient.invalidateQueries({ queryKey: queryKeys.account(broker, variables.accountNo) });
      queryClient.invalidateQueries({ queryKey: queryKeys.market(broker, variables.symbol) });
    }
  });
}