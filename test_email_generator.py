import random
import json

def generate_random_string(length=8):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_po():
    return str(random.randint(40000, 50000))

def generate_random_part_no():
    parts = [
        "Catamount 8L RI Rev 1 & Catamount 8L REStripline",
        "PT-0037229 Rev A PT-0038573 Rev A",
        "Dual Sensor V2.0",
        "Panel_CAM81204140_01",
        "DA0961 SMTPA PCB V1P3",
        "FT-0093472 Rev B FT-0048723 Rev C",
        "Quad Sensor V3.1",
        "Module_XYZ12457890_A",
        "AX2045 SMTAB PCB V2Q5",
    ]
    return random.choice(parts)

def generate_random_quantity():
    return str(random.randint(1, 500))

def generate_random_tracking_number():
    return str(random.randint(1000000000, 9999999999))

def generate_random_name():
    first_names = ["Tom", "Niall", "Sarah", "Emily", "James", "Oliver", "Sophia", "Isabella", "Liam", "Mason"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_test_email():
    po_numbers = [generate_random_po() for _ in range(5)]
    part_numbers = [generate_random_part_no() for _ in range(5)]
    quantities = [generate_random_quantity() for _ in range(5)]
    tracking_number = generate_random_tracking_number()
    sender_name = generate_random_name()
    recipient_name = generate_random_name()
    
    while recipient_name == sender_name:
        recipient_name = generate_random_name()
    
    email_content = f"""
    Hi {recipient_name.split()[0]},
    See below shipment:
    | PO    | Part No.                                         | Pnl  |
    |-------|--------------------------------------------------|------|
    | {po_numbers[0]} | {part_numbers[0]} | {quantities[0]}    |
    | {po_numbers[1]} | {part_numbers[1]} | {quantities[1]}    |
    | {po_numbers[2]} | {part_numbers[2]} | {quantities[2]}    |
    | {po_numbers[3]} | {part_numbers[3]} | {quantities[3]}    |
    | {po_numbers[4]} | {part_numbers[4]} | {quantities[4]}    |
    DHL: {tracking_number} 
    {sender_name}
    Sales Manager
    <Attachment: Commercial Invoice {generate_random_string()}>"""
    
    labels = {
        "po_numbers": po_numbers,
        "part_numbers": part_numbers,
        "quantities": quantities,
        "tracking_number": tracking_number
    }
    
    return {
        "sender": sender_name,
        "recipient": recipient_name,
        "subject": "Shipment Notification",
        "body": email_content,
        "labels": labels
    }

def generate_test_emails(num_emails=30):
    test_emails = [generate_test_email() for _ in range(num_emails)]
    with open('labeled_test_emails.json', 'w') as f:
        json.dump(test_emails, f, indent=4)

# Generate 30 test emails and save to a JSON file
generate_test_emails()
