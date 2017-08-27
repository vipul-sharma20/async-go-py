package main

import (
    "fmt"
    "net/http"
)


func main() {
    url := "http://example.com"
    resc, errc := make(chan bool), make(chan error)

    for i := 0; i < 1000; i++ {
        go func(url string) {
            _, err := http.Get(url)
            if err != nil {
                errc <- err
                return
            }
            resc <- true
        }(url)
    }
    for i := 0; i < 1000; i++ {
        select {
        case <-resc:
        case err := <-errc:
            fmt.Println(err)
        }
    }
}
