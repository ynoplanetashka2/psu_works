type Styles = React.HTMLAttributes<HTMLDivElement>['style'];
type Props = { children: React.ReactNode; style?: Styles; onClick?: () => void; };

export function OpticToolsItem({ children, onClick, style = {} }: Props) {
  return (
    <li style={style} onClick={onClick}>
        {children}
    </li>
  );
}
