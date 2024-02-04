import { useMeasure } from "react-use";

type Props = {
  style?: React.HTMLAttributes<SVGSVGElement>["style"];
};

export function BeamPath({ style = {} }: Props) {
  const [containerRef, { width, height }] = useMeasure<SVGSVGElement>();
  const pathLine = width > 0 ? `M0 0 L${width} ${height}` : "";
  return (
    <svg style={style} ref={containerRef}>
      <path
        d={pathLine}
        style={{
          stroke: "black",
          strokeWidth: "2px",
          fill: "none",
        }}
      />
    </svg>
  );
}
