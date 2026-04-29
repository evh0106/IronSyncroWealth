import { create } from "zustand";
import { persist } from "zustand/middleware";
import type { Broker } from "@/shared/api/client";

type ThemeMode = "sunrise" | "midnight";

type UiState = {
  broker: Broker;
  theme: ThemeMode;
  sidebarOpen: boolean;
  setBroker: (broker: Broker) => void;
  setTheme: (theme: ThemeMode) => void;
  toggleSidebar: () => void;
};

export const useUiStore = create<UiState>()(
  persist(
    (set) => ({
      broker: "kiwoom",
      theme: "sunrise",
      sidebarOpen: true,
      setBroker: (broker) => set({ broker }),
      setTheme: (theme) => set({ theme }),
      toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen }))
    }),
    { name: "isw-ui" }
  )
);