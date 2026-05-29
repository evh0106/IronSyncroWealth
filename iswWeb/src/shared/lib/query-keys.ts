export const queryKeys = {
  account: (broker: string, accountNo: string) => ["account", broker, accountNo] as const,
  market: (broker: string, symbol: string) => ["market", broker, symbol] as const,
  orders: (broker: string, accountNo: string) => ["orders", broker, accountNo] as const
};