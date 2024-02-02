import React from "react";
import { Lens } from "./Lens";

type Styles = React.HTMLAttributes<HTMLDivElement>['style'];
type Props = { style?: Styles; onClick?: (ratio: number) => void; };

function getRelativeMouseXPosition(event: React.MouseEvent): number {
  const targetElement: any = event.nativeEvent.target;
  const rect = targetElement.getBoundingClientRect();
  const width = rect.right - rect.left;
  const xDiff = event.clientX - rect.left;
  return xDiff / width;
}

export function MainOpticLine({ style = {}, onClick }: Props) {
  function handleClick(event: React.MouseEvent) {
    const relativePosition = getRelativeMouseXPosition(event);
    onClick && onClick(relativePosition);
  }
  return (
    <div
      style={{
        background: "black",
        ...style,
      }}
      onClick={handleClick}
    >
      <div>
        <Lens
            style={{
                width: '20px',
                height: '200px',
            }}
        />
      </div>
    </div>
  );
}
