def get_contacts(filename):
    names = []
    emails = []
    with open(filename,mode='r',encoding='utf-8') as contact_list:
        for contact in contact_list:
            names.append(contact.split()[0])
            emails.append(contact.split()[1])
    return names, emails
