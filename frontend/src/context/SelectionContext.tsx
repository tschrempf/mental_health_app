import React, { createContext, useContext, useState } from "react";

interface SelectionContextType {
  selections: { [key: string]: string };
  setSelection: (page: string, value: string) => void;
}

const SelectionContext = createContext<SelectionContextType | undefined>(undefined);

export const SelectionProvider: React.FC<React.PropsWithChildren<object>> = ({ children }) => {
  const [selections, setSelections] = useState<{ [key: string]: string }>({});

  const setSelection = (page: string, value: string) => {
    setSelections((prev) => ({ ...prev, [page]: value }));
  };

  return <SelectionContext.Provider value={{ selections, setSelection }}>{children}</SelectionContext.Provider>;
};

export const useSelection = () => {
  const context = useContext(SelectionContext);
  if (!context) {
    throw new Error("useSelection must be used within a SelectionProvider");
  }
  return context;
};
