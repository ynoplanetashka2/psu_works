import { BeamVectorSettings } from "./BeamVectorSettings";
import { LensSettings } from "./LensSettings";

type Props = {
  style?: React.HTMLAttributes<HTMLDivElement>["style"];
};

export function OpticsObjectsSettings({ style = {} }: Props) {
  return (
    <div style={style}>
      <BeamVectorSettings />
      <LensSettings />
    </div>
  );
}
