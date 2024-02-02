import { MainOpticLine } from "./MainOpticLine";

type Props = {
  style?: React.HTMLAttributes<HTMLDivElement>["style"];
};

export function OpticCanvas({ style = {} }: Props) {
  return (
    <div
      style={{
        background: "pink",
        position: "relative",
        ...style,
      }}
    >
      <MainOpticLine
        style={{
          width: "100%",
          height: "10px",
          position: "absolute",
          top: "220px",
        }}
        onClick={(ratio) => void console.log(ratio)}
      />
    </div>
  );
}
