from django.contrib import admin
from .models import login,city,state,feedback,biodata,choices,contact,detail,savelist
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def export_to_pdf(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 14),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers = ['email','phone','status']

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.email, obj.phone, obj.status])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description = "Export to PDF"

# Register your models here.

class showusers(admin.ModelAdmin):
    list_display = ['email','phone','password','dp','role','status']
    actions = [export_to_pdf]


admin.site.register(login,showusers)


class showfeedback(admin.ModelAdmin):
    list_display = ['lid','ratings','comment']

admin.site.register(feedback,showfeedback)


class showcity(admin.ModelAdmin):
    list_display = ['cityname','stateid']

admin.site.register(city,showcity)


class showstate(admin.ModelAdmin):
    list_display = ['statename']

class showcontact(admin.ModelAdmin):
    list_display = ['name','email','subject','message']

admin.site.register(state,showstate)
admin.site.register(biodata)
admin.site.register(savelist)
admin.site.register(choices)
admin.site.register(detail)
admin.site.register(contact,showcontact)
