import { Lens } from "./Lens";
import { MainOpticLine } from "./MainOpticLine";

type LensInfo = {
  position: number;
  id: string;
};
type Props = {
  style?: React.HTMLAttributes<HTMLDivElement>["style"];
  lens: ReadonlyArray<LensInfo>;
};

export function OpticCanvas({ style = {}, lens }: Props) {
  return (
    <div
      style={{
        background: "pink",
        position: "relative",
        ...style,
      }}
    >
      {lens.map(({ position, id }) => (
        <Lens
          style={{
            position: "absolute",
            left: `${position * 100}%`,
            height: "100%",
            zIndex: 2,
          }}
          key={id}
        />
      ))}
      <MainOpticLine
        style={{
          width: "100%",
          height: "10px",
          position: "absolute",
          top: "calc((100% - 10px) / 2)",
          zIndex: 1,
        }}
        onClick={(ratio) => void console.log(ratio)}
      />
    </div>
  );
}
