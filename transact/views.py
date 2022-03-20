from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from transact.models import TransactionDetail, Customer
from transact.forms import Transaction_form

def index(request):
    return render(request, 'home.html')

def makeTransaction(request):
    form = Transaction_form()
    if request.method == "POST":
        form = Transaction_form(request.POST)
        if form.is_valid():
            fromCust = form.cleaned_data['fromCust']
            toCust = form.cleaned_data['toCust']
            payment = form.cleaned_data['payment']
            presentFrom = Customer.objects.filter(custName=fromCust)
            if presentFrom.exists():
                presentTo = Customer.objects.filter(custName=toCust)
                if presentTo.exists():
                    fromDet = Customer.objects.get(custName=fromCust)
                    if fromDet.custBalance >= payment:
                        if payment > 0:
                            toDet = Customer.objects.get(custName=toCust)
                            fromDet.custBalance -= payment
                            fromDet.save()
                            toDet.custBalance += payment
                            toDet.save()
                            form.save()
                            return render(request, 'makeTransaction.html',{'message': 'Payment made successfully.'})
                        else:
                            return render(request, 'makeTransaction.html',{'message': 'Enter valid amount.'})
                    else:
                        return render(request, 'makeTransaction.html',{'message': 'Insufficient Balance.'})
                else:
                    return render(request, 'makeTransaction.html',{'message': 'Recipient does not exist. Enter valid recipient name.'})
            else:
                return render(request, 'makeTransaction.html',{'message': 'This customer does not exist. Enter valid customer name.'})
    return render(request, 'makeTransaction.html', {'form': form})

def displayTransaction(request):
    transaction = TransactionDetail.objects.all()
    return render(request, 'displayTrans.html', context = {"transaction": transaction})

def displayCustomer(request):
    customer = Customer.objects.all()
    return render(request, 'displayCust.html', context = {"customer": customer})