from django.urls import path
from . import views
from .views import ( 
    WasteListView,
    AddToListView,
    UpdateListView,
    DeleteItemListView,
    WasteImgView,
    CreateInvoiceView,
    DeleteInvoiceView,
    SalesView,
    AddItemsToInvoiceView,
    InvoiceDetailView,
    GeneratePdf,
    )


urlpatterns = [
    
    #URLS FOR HOME AND WASTEITEMS
    path("", views.home, name="pw-home"),
    path("waste/", WasteImgView.as_view(), name="pw-food"),
    path("wastelist/", WasteListView.as_view(), name="pw-foodlist"),
    path('dashboard/addtolist',AddToListView.as_view(),name="pw-addtolist"),
    path('wastelist/<int:pk>/delete/',DeleteItemListView.as_view(),name="waste_confirm_delete"),
    path('dashboard/addtolist/<int:pk>/update/',UpdateListView.as_view(),name="pw-updatetolist"),

    #URLS FOR INVOICES
    path('dashboard/createinvoice', CreateInvoiceView.as_view(), name='createinvoice'),
    path("dashboard/sales", SalesView.as_view(), name="sales"),
    path("invoices/<int:pk>", AddItemsToInvoiceView.as_view(), name="add_items_on_invoice"),
    path("invoices/<int:pk>/details", InvoiceDetailView.as_view(), name="invoice_details"),
    path('dashboard/sales/<int:pk>/delete/',DeleteInvoiceView.as_view(),name="invoice_confirm_delete"),
    path('invoices/<int:pk>/details/print', GeneratePdf.as_view(), name="invoice_print"),
]
