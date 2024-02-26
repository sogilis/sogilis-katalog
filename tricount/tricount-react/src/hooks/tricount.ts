import {useEffect} from "react";

export function useTricount() {
    useEffect(() => {
        (async() => {
            await getTricounts()
        })()
    }, []);

    return { tricounts: [] };
}

function getTricounts() {
    return Promise.reject("Method not implemented.");
}