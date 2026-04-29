import { QueryProvider } from "@/app/providers/query-provider";
import { RouterAppProvider } from "@/app/providers/router-provider";

export function App() {
  return (
    <QueryProvider>
      <RouterAppProvider />
    </QueryProvider>
  );
}