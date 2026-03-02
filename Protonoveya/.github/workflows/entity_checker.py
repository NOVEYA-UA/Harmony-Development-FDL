import json

def evaluate_entity(name, has_contract, frequency_ok, uses_grants):
    """
    name: Назва сутності
    has_contract: Наявність прямого договору з Громадою (True/False)
    frequency_ok: Дотримання стандарту 7.83 Гц (True/False)
    uses_grants: Використання зовнішніх грантів (True/False)
    """
    score = 0
    if has_contract: score += 40
    if frequency_ok: score += 40
    if not uses_grants: score += 20
    
    status = "СВІЙ (FRIEND)" if score >= 80 else "НЕЙТРАЛ (NEUTRAL)" if score >= 40 else "ЧУЖИЙ (RISK)"
    
    print(f"\n--- ПЕРЕВІРКА СУБ'ЄКТНОСТІ: {name} ---")
    print(f"Рейтинг Резонансу: {score}/100")
    print(f"СТАТУС: {status}")
    
    if status == "ЧУЖИЙ (RISK)":
        print("[!] УВАГА: Ризик паразитарного впливу. Рекомендується режим Ізоляції.")

if __name__ == "__main__":
    # Тест: представник водоканалу без договору
    evaluate_entity("МКП Водоканал", has_contract=False, frequency_ok=False, uses_grants=True)
    # Тест: сусідська община
    evaluate_entity("Община Сафронівки", has_contract=True, frequency_ok=True, uses_grants=False)
