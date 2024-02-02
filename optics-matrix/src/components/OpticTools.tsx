import { OpticToolsItem } from "./OpticToolsItem";

type Styles = React.HTMLAttributes<HTMLUListElement>['style'];
type Props = { 
    style?: Styles;
    onLensAdd: () => void;
    onElementRemove: () => void;
    onElementConfig: () => void;
 };

export function OpticTools({ style = {}, onLensAdd, onElementRemove, onElementConfig }: Props) {
    return (
        <ul style={{
            listStyleType: 'none',
            display: 'flex',
            flexDirection: 'row',
            marginLeft: '10px',
            padding: '5px',
            ...style
        }}>
            <OpticToolsItem 
                style={{ marginRight: '10px', background: 'green'}}
                onClick={onLensAdd}
                >
                Добавить линзу
            </OpticToolsItem>
            <OpticToolsItem 
                style={{ marginRight: '10px', background: 'green'}}
                onClick={onElementRemove}
            >
                Удалить элемент
            </OpticToolsItem>
            <OpticToolsItem 
                style={{ background: 'green' }}
                onClick={onElementConfig}
                >
                Настроить элемент
            </OpticToolsItem>
        </ul>
    )
}