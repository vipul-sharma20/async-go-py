package main

import (
    "fmt"
    "net/http"
)


func main() {
    url := "http://thecatapi.com/api/images/get?type=jpg"
    done := make(chan bool)

    for i := 0; i < 5; i++ {
        go func(url string) {
            response, err := http.Get(url)
            if err != nil {
                fmt.Println("Error occurred")
            } else {
                fmt.Println(response)
            }
            done <- true
        }(url)
    }
    for i := 0; i < 5; i++ {
        <-done
    }
}
