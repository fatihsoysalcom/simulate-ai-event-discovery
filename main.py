import re

# Simulated Ticketmaster Event Database
# In a real scenario, this would be a vast, dynamic database accessed via API.
EVENTS = [
    {"id": 1, "name": "Rock Fest İstanbul", "city": "İstanbul", "type": "Konser", "genre": "Rock", "price": "Orta", "date": "Bu hafta sonu"},
    {"id": 2, "name": "Ankara Tiyatro Günleri", "city": "Ankara", "type": "Tiyatro", "genre": "Drama", "price": "Uygun", "date": "Gelecek hafta"},
    {"id": 3, "name": "Pop Yıldızları Konseri", "city": "İstanbul", "type": "Konser", "genre": "Pop", "price": "Yüksek", "date": "Bu hafta sonu"},
    {"id": 4, "name": "İzmir Komedi Festivali", "city": "İzmir", "type": "Tiyatro", "genre": "Komedi", "price": "Orta", "date": "Bu ay"},
    {"id": 5, "name": "Klasik Müzik Akşamı", "city": "Ankara", "type": "Konser", "genre": "Klasik", "price": "Uygun", "date": "Bu hafta sonu"},
    {"id": 6, "name": "Dans Gösterisi", "city": "İstanbul", "type": "Dans", "genre": "Modern", "price": "Orta", "date": "Gelecek hafta"},
    {"id": 7, "name": "Futbol Maçı: Fenerbahçe vs Galatasaray", "city": "İstanbul", "type": "Spor", "genre": "Futbol", "price": "Yüksek", "date": "Bu hafta sonu"},
    {"id": 8, "name": "Ankara Sanat Sergisi", "city": "Ankara", "type": "Sergi", "genre": "Sanat", "price": "Uygun", "date": "Bu ay"},
]

def gemini_event_discovery(query: str) -> list[dict]:
    """
    Simulates Google Gemini's ability to understand natural language queries
    and filter a database of events.
    """
    query_lower = query.lower()
    
    # --- Simulate NLP and contextual understanding ---
    # This section mimics how an AI like Gemini would parse user intent
    # and extract key entities (city, event type, price, date) from a natural language query.
    filters = {}
    
    # City detection
    if "istanbul" in query_lower:
        filters["city"] = "İstanbul"
    elif "ankara" in query_lower:
        filters["city"] = "Ankara"
    elif "izmir" in query_lower:
        filters["city"] = "İzmir"

    # Event type/genre detection
    if "rock konser" in query_lower or "rock konserleri" in query_lower:
        filters["type"] = "Konser"
        filters["genre"] = "Rock"
    elif "tiyatro" in query_lower:
        filters["type"] = "Tiyatro"
    elif "konser" in query_lower:
        filters["type"] = "Konser"
    elif "spor" in query_lower or "maç" in query_lower:
        filters["type"] = "Spor"
    elif "dans" in query_lower:
        filters["type"] = "Dans"
    elif "sergi" in query_lower:
        filters["type"] = "Sergi"
    
    # Price detection
    if "uygun fiyatlı" in query_lower or "ucuz" in query_lower:
        filters["price"] = "Uygun"
    elif "orta fiyatlı" in query_lower:
        filters["price"] = "Orta"
    elif "pahalı" in query_lower or "yüksek fiyatlı" in query_lower:
        filters["price"] = "Yüksek"

    # Date detection
    if "bu hafta sonu" in query_lower:
        filters["date"] = "Bu hafta sonu"
    elif "gelecek hafta" in query_lower:
        filters["date"] = "Gelecek hafta"
    elif "bu ay" in query_lower:
        filters["date"] = "Bu ay"

    # --- Filter the simulated event database ---
    # This represents Gemini accessing Ticketmaster's event data and applying the parsed filters.
    results = []
    for event in EVENTS:
        match = True
        for key, value in filters.items():
            # Case-insensitive and partial matching for flexibility
            if key == "city" and value.lower() not in event[key].lower():
                match = False
                break
            elif key == "type" and value.lower() not in event[key].lower():
                match = False
                break
            elif key == "genre" and value.lower() not in event.get(key, "").lower(): # genre might not always be present
                match = False
                break
            elif key == "price" and value.lower() not in event[key].lower():
                match = False
                break
            elif key == "date" and value.lower() not in event[key].lower():
                match = False
                break
        if match:
            results.append(event)
            
    return results

def format_event(event: dict) -> str:
    """Helper to format event details for display."""
    details = [
        f"Etkinlik: {event['name']}",
        f"Şehir: {event['city']}",
        f"Tür: {event['type']}",
    ]
    if 'genre' in event and event['genre']:
        details.append(f"Tarz: {event['genre']}")
    details.append(f"Fiyat Seviyesi: {event['price']}")
    details.append(f"Tarih İpucu: {event['date']}")
    return "\n  ".join(details)

if __name__ == "__main__":
    print("Google Gemini Etkinlik Keşfi Simülasyonu")
    print("Örnek sorgular: 'İstanbul'da bu hafta sonu hangi rock konserleri var?'")
    print("                 'Ankara'da uygun fiyatlı tiyatro oyunları neler?'")
    print("                 'Bu ay İzmir'de komedi gösterileri var mı?'")
    print("Çıkmak için 'çıkış' yazın.")
    print("-" * 50)

    while True:
        user_query = input("\nSorgunuz: ")
        if user_query.lower() == "çıkış":
            break

        # --- This is where the Gemini-Ticketmaster integration concept is demonstrated ---
        # Gemini processes the natural language query and translates it into actionable filters
        # to query the event database.
        found_events = gemini_event_discovery(user_query)

        if found_events:
            print("\nİşte sizin için bulduğum etkinlikler:")
            for event in found_events:
                print(f"--- Etkinlik ID: {event['id']} ---")
                print(format_event(event))
                print("--------------------")
        else:
            print("\nÜzgünüm, sorgunuza uygun etkinlik bulunamadı.")
            print("Lütfen farklı bir sorgu deneyin veya daha genel bir arama yapın.")
