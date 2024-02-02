type Styles = React.HTMLAttributes<HTMLImageElement>["style"];
type Props = { style?: Styles; onClick?: () => void };

export function Lens({ style, onClick }: Props) {
  return (
    <img
      alt="lens"
      src="./lens.png"
      style={style}
      onClick={() => onClick && onClick()}
    />
  );
}
