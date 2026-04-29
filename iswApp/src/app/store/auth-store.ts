import { create } from "zustand";
import { persist } from "zustand/middleware";

type AuthState = {
  accessToken: string | null;
  userId: string | null;
  setSession: (accessToken: string, userId: string) => void;
  clearSession: () => void;
};

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      accessToken: null,
      userId: null,
      setSession: (accessToken, userId) => set({ accessToken, userId }),
      clearSession: () => set({ accessToken: null, userId: null })
    }),
    { name: "isw-auth" }
  )
);