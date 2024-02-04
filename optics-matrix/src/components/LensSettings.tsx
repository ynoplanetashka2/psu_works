import { useId } from "react";

type LensInfo = {
  position: number;
  refractionCoeff: number;
  radiusOfCurvature: number;
};
type Props = {
  style?: React.HTMLAttributes<HTMLDivElement>["style"];
  lensInfo: LensInfo;
  onUpdateLensInfo: (_: LensInfo) => void;
};

export function LensSettings({
  style = {},
  lensInfo,
  onUpdateLensInfo,
}: Props) {
  const inputsId = useId();
  const positionInputId = `${inputsId}-position-input`;
  const refractionCoeffInputId = `${inputsId}-refract-coeff-input`;
  const radiusOfCurvatureInputId = `${inputsId}-radius-of-curvature-input`;
  function handlePositionChange(event: React.ChangeEvent<HTMLInputElement>) {
    onUpdateLensInfo({
      ...lensInfo,
      position: Number(event.target.value),
    });
  }
  function handleRefractionCoeffChange(
    event: React.ChangeEvent<HTMLInputElement>
  ) {
    onUpdateLensInfo({
      ...lensInfo,
      refractionCoeff: Number(event.target.value),
    });
  }
  function handleRadiusOfCurvatureChange(
    event: React.ChangeEvent<HTMLInputElement>
  ) {
    onUpdateLensInfo({
      ...lensInfo,
      radiusOfCurvature: Number(event.target.value),
    });
  }
  return (
    <div
      style={{
        background: "purple",
        ...style,
      }}
    >
      <fieldset>
        <label htmlFor={positionInputId}>position: </label>
        <input
          id={positionInputId}
          onChange={handlePositionChange}
          value={lensInfo.position}
        />
        <label htmlFor={refractionCoeffInputId}>refraction coeff: </label>
        <input
          id={refractionCoeffInputId}
          onChange={handleRefractionCoeffChange}
          value={lensInfo.refractionCoeff}
        />
        <label htmlFor={radiusOfCurvatureInputId}>radius of curvature: </label>
        <input
          id={radiusOfCurvatureInputId}
          onChange={handleRadiusOfCurvatureChange}
          value={lensInfo.radiusOfCurvature}
        />
      </fieldset>
    </div>
  );
}
