import { OpticAppState } from "../hooks/useOpticApp";
import { OpticToolsItem } from "./OpticToolsItem";

type Styles = React.HTMLAttributes<HTMLUListElement>["style"];
type Props = {
  style?: Styles;
  onLensAdd: () => void;
  onElementRemove: () => void;
  onElementConfig: () => void;
  opticAppState: OpticAppState;
};

export function OpticTools({
  style = {},
  onLensAdd,
  onElementRemove,
  onElementConfig,
  opticAppState,
}: Props) {
  return (
    <ul
      style={{
        listStyleType: "none",
        display: "flex",
        flexDirection: "row",
        marginLeft: "10px",
        padding: "5px",
        ...style,
      }}
    >
      <OpticToolsItem
        style={{
          marginRight: "10px",
          background: opticAppState === "addLens" ? "yellow" : "green",
          cursor: "pointer",
        }}
        onClick={onLensAdd}
      >
        Добавить линзу
      </OpticToolsItem>
      <OpticToolsItem
        style={{
          marginRight: "10px",
          background: opticAppState === "removeLens" ? "yellow" : "green",
          cursor: "pointer",
        }}
        onClick={onElementRemove}
      >
        Удалить элемент
      </OpticToolsItem>
      <OpticToolsItem
        style={{
          background: opticAppState === "configLens" ? "yellow" : "green",
          cursor: "pointer",
        }}
        onClick={onElementConfig}
      >
        Настроить элемент
      </OpticToolsItem>
    </ul>
  );
}
