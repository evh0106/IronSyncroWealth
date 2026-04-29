import { useUiStore } from "@/app/store/ui-store";

export function useBrokerSwitch() {
  const broker = useUiStore((state) => state.broker);
  const setBroker = useUiStore((state) => state.setBroker);
  return { broker, setBroker };
}