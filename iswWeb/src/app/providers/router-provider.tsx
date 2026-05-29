import { RouterProvider } from "react-router-dom";
import { appRouter } from "@/app/routes";

export function RouterAppProvider() {
  return <RouterProvider router={appRouter} />;
}