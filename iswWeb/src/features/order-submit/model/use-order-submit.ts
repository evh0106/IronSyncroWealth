import { useMemo, useState } from "react";
import { useUiStore } from "@/app/store/ui-store";
import { useSubmitOrder } from "@/entities/order/api/mutations";

export function useOrderSubmit() {
  const broker = useUiStore((state) => state.broker);
  const mutation = useSubmitOrder(broker);

  const [accountNo, setAccountNo] = useState("81241972");
  const [symbol, setSymbol] = useState("005930");
  const [side, setSide] = useState<"buy" | "sell">("buy");
  const [quantity, setQuantity] = useState(1);
  const [price, setPrice] = useState(70000);

  const canSubmit = useMemo(() => quantity > 0 && price > 0 && symbol.length > 0, [quantity, price, symbol]);

  const submit = async () => {
    if (!canSubmit) return;
    await mutation.mutateAsync({ accountNo, symbol, side, quantity, price });
  };

  return {
    accountNo,
    symbol,
    side,
    quantity,
    price,
    setAccountNo,
    setSymbol,
    setSide,
    setQuantity,
    setPrice,
    submit,
    canSubmit,
    isPending: mutation.isPending,
    isSuccess: mutation.isSuccess,
    error: mutation.error
  };
}