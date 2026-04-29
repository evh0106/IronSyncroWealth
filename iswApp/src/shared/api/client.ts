import axios from "axios";
import { env } from "@/shared/config/env";

export type Broker = "kiwoom" | "kis";

const clients = {
  kiwoom: axios.create({ baseURL: env.kiwoomBaseUrl, timeout: 10_000 }),
  kis: axios.create({ baseURL: env.kisBaseUrl, timeout: 10_000 })
};

export function setAuthToken(token: string | null) {
  const value = token ? `Bearer ${token}` : undefined;
  clients.kiwoom.defaults.headers.common.Authorization = value;
  clients.kis.defaults.headers.common.Authorization = value;
}

export function apiClient(broker: Broker) {
  return clients[broker];
}