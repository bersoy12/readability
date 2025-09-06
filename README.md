# Readability Microservice

Bu proje, **web sayfalarındaki gereksiz içerikleri (reklam, menü, footer vb.) temizleyip** sadeleştirilmiş metin döndüren basit bir microservice sunar.  
**n8n** üzerinde HTTP Request node ile kullanarak haberleri veya makaleleri temiz içerik halinde işleyebilirsiniz.  

## Çalıştırma

```bash
docker build -t readability-service .
docker run -p 5000:5000 readability-service
```


## Kullanım

URL'i JSON body ile gönderin:

```bash
curl -X POST http://localhost:5000/readability \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.atlanticcouncil.org/content-series/fastthinking/twenty-six-european-countries-have-committed-to-help-defend-ukraine-after-the-war-whats-next/"}'
```


## Alternatif: Tarayıcıdan çağrım yapılacaksa

```bash
http://localhost:5000/readability?url=https://www.atlanticcouncil.org/content-series/fastthinking/twenty-six-european-countries-have-committed-to-help-defend-ukraine-after-the-war-whats-next/
```