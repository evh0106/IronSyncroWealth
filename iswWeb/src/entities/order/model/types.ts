export type OrderRequest = {
  accountNo: string;
  symbol: string;
  side: "buy" | "sell";
  quantity: number;
  price: number;
};

export type OrderResponse = {
  orderId: string;
  status: string;
};