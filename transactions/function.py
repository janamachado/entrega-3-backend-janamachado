from .models import Transaction


def handle_uploaded_file(f):
    with open('static/uploads/cnab.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    with open('static/uploads/cnab.txt', 'r') as listInfos:
        file_infos = []
        for file in listInfos:
            file_infos.append(file)
    
    for item in file_infos:
            type = item[:1]
            year = item[1:5]
            month = item[5:7]
            day = item[7:9]
            value = item[9:19]
            cpf = item[19:30]
            card = item[30:42]
            hour = item[42:44]
            minute = item[44:46]
            second = item[46:48]
            shop_owner = item[48:62]
            shop_name = item[62:81]

            date = f"{day}/{month}/{year}"
            value = int(value) / 100
            time = f"{hour}:{minute}:{second}"

            Transaction.objects.create(
                type=type,
                date=date,
                value=value,
                cpf=cpf,
                card=card,
                hour=time,
                shop_owner=shop_owner,
                shop_name=shop_name,
            )