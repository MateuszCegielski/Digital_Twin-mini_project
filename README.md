# Authors
Mateusz Cegielski
Daniel Augusto


# Warm-Up

## Zalożenia projektu 

W ramach rozgrzewki zaprogramujemy uproszczoną wersję digital twina.
Ogarniemy w ten sposób ogólną zasadę działania programu, pracę z gihubem,
konfigurację IDE i stosowanie dobrych praktyk programistycznych.

## Wymagania:
1. Program będzie przyjmował dwa pliki wejściowe, jeden z danymi z czujników (prędkość, moment obrotowy) w formacie csv, a drugi z informacjami konfiguracyjnymi (parametry łożysk, wałów itp) w formacie json.
2. Program będzie zwracał wyniki w formacie json.
3. Program ma liczyć na podstawie danych wejściowych długość życia łożysk (L10)
i statyczny współczynnik bezpieczeństwa dla wałów.
4. Program powinien umożliwić skonfigurowanie kilku różnych łożysk i wałów, w taki
sposób, że wyniki będą policzone do każdego z nich.
5. Sama implementacja od strony mechanicznej nie jest najważniejsza; jak nie wygooglujecie
to was naprowadzę.
6. Kod powinien znaleźć się na githubie w otwartym repozytorium.
7. Kod powinien być pisany zgodnie z wytycznymi, które podeślę na teamsie.
8. Projekt jest mocno "otwarty" i nie ma jednego własciwego rozwiązania. Spróbujcie się
dogadać między sobą i podzielić pracą ;)

## Obsługa aplikacji 
Jeśli nie posiadasz swoich danych, możesz je wygenerować automatycznie uruchamiając plik "data_generation", nastepnie należy uruchomić "main" aby uzyskać policzone wyniki dla podanych obiektów w pliku JSON i pomiarów z pliku CSV. Uzyskany wynik jest exportowany w formacie JSON. Pamiętaj, aby uzupełnić odpowednio ścieżki w pliku "main" do plików, które chcesz przetworzyć. 

Enjoy! 
