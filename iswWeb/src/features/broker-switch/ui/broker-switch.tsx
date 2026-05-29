import { useBrokerSwitch } from "@/features/broker-switch/model/use-broker-switch";

export function BrokerSwitch() {
  const { broker, setBroker } = useBrokerSwitch();

  return (
    <div className="broker-switch">
      <button
        className={broker === "kiwoom" ? "active" : ""}
        onClick={() => setBroker("kiwoom")}
        type="button"
      >
        Kiwoom
      </button>
      <button
        className={broker === "kis" ? "active" : ""}
        onClick={() => setBroker("kis")}
        type="button"
      >
        KIS
      </button>
    </div>
  );
}