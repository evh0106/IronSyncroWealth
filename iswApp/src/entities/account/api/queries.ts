import { useQuery } from "@tanstack/react-query";
import type { Broker } from "@/shared/api/client";
import { apiClient } from "@/shared/api/client";
import { queryKeys } from "@/shared/lib/query-keys";
import type { AccountSummary } from "@/entities/account/model/types";

export function useAccountSummary(broker: Broker, accountNo: string) {
  return useQuery({
    queryKey: queryKeys.account(broker, accountNo),
    queryFn: async () => {
      const { data } = await apiClient(broker).get<AccountSummary>(`/api/v1/account/${accountNo}/summary`);
      return data;
    },
    staleTime: 30_000
  });
}