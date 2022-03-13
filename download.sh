#!/bin/sh

# Download prepared data and extract it
curl https://pajda.fit.vutbr.cz/ios/ios-22-1-inputs/-/archive/main/ios-22-1-inputs-main.tar.gz?path=data | tar -xzv --strip-components=1

# Download latest data
curl https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/osoby.csv -o data/latest.csv
