from docxtpl import DocxTemplate


def create_training_sheet(class_name, subject_name, tpl_name, *args):
    doc = DocxTemplate(tpl_name)
    args = [{'num': i + 1,
             'fio': j[0], 'mark': j[1]} for i, j in enumerate(sorted(args, key=lambda x: x[0]))]
    context = {
        'class_name': class_name,
        'subject_name': subject_name,
        'marks': args
    }
    doc.render(context)
    doc.save("res.docx")
