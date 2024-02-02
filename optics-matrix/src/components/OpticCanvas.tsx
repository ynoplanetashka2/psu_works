import { Lens } from "./Lens";
import { MainOpticLine } from "./MainOpticLine";
import { OpticTools } from "./OpticTools";

export function OpticCanvas() {
    return (
        <div style={{
            width: '980px',
            height: '400px',
            background: 'grey',
            position: 'relative',
        }}>
            <OpticTools 
                style={{
                    position: 'absolute',
                    background: 'pink',
                }}
                onElementConfig={() => void console.log('config')}
                onElementRemove={() => void console.log('remove')}
                onLensAdd={() => void console.log('add')}
            />
            <MainOpticLine 
                style={{
                    width: '100%',
                    height: '10px',
                    position: 'absolute',
                    top: '220px',
                }} 
                onClick={(ratio) => void console.log(ratio)}
            />
        </div>
    );
}