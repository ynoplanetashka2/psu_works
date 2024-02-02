type Styles = React.HTMLAttributes<HTMLImageElement>['style'];
type Props = { style?: Styles; };

export function Lens({ style }: Props) {
    return (
        <img 
            alt="lens" 
            src="./lens.png"
            style={style}
        />
    );
}