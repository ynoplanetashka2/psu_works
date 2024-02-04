import { useId } from "react";
import { BeamVector } from "../optics-matrix-model/BeamVector";

type Props = {
  style?: React.HTMLAttributes<HTMLDivElement>["style"];
  beamVector: BeamVector;
  onUpdateBeamVector: (_: BeamVector) => void;
};

export function BeamVectorSettings({
  style = {},
  beamVector,
  onUpdateBeamVector,
}: Props) {
  const inputsId = useId();
  const heightInputId = `${inputsId}-height-input`;
  const angleInputId = `${inputsId}-angle-input`;
  function handleHeightChange(event: React.ChangeEvent<HTMLInputElement>) {
    onUpdateBeamVector([Number(event.target.value), beamVector[1]]);
  }
  function handleAngleChange(event: React.ChangeEvent<HTMLInputElement>) {
    onUpdateBeamVector([beamVector[0], Number(event.target.value)]);
  }
  return (
    <div
      style={{
        background: "purple",
        ...style,
      }}
    >
      <fieldset>
        <label htmlFor={heightInputId}>height: </label>
        <input
          id={heightInputId}
          onChange={handleHeightChange}
          value={beamVector[0]}
        />
        <label htmlFor={angleInputId}>angle: </label>
        <input
          id={angleInputId}
          onChange={handleAngleChange}
          value={beamVector[1]}
        />
      </fieldset>
    </div>
  );
}
