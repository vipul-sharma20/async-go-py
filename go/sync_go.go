package main

import(
    "fmt"
    "net/http"
)

func main() {
    url := "http://example.com"

    for i := 1; i < 1000; i++ {
        _, err := http.Head(url)
        if err != nil {
            fmt.Println(err)
        }
    }
}
