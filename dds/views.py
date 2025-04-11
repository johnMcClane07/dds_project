from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import CashFlow, Status, Type, Category, Subcategory
from .forms import CashFlowForm, StatusForm, TypeForm, CategoryForm, SubcategoryForm

def common_create_or_edit(request, model, form_class, pk=None, action_title=None, list_url=None):
    """
    Универсальная функция для создания или редактирования объекта модели.

    :param request: Объект запроса
    :param model: Модель, с которой производится работа
    :param form_class: Форма для модели
    :param pk: Идентификатор объекта для редактирования (если None — создание нового)
    :param action_title: Название действия (например, создание или редактирование)
    :param list_url: URL для редиректа после успешного сохранения
    :return: Рендеринг шаблона с формой
    """
    if pk:
        obj = get_object_or_404(model, pk=pk)
    else:
        obj = None

    if request.method == 'POST':
        form = form_class(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(list_url)
    else:
        form = form_class(instance=obj)

    context = {
        'form': form,
        'action': action_title
    }

    return render(request, 'common_form.html', context)

def common_confirm_delete(request, model, pk, list_url):
    """
    Универсальная функция для подтверждения удаления объекта модели.

    :param request: Объект запроса
    :param model: Модель, с которой производится работа
    :param pk: Идентификатор объекта для удаления
    :param list_url: URL для редиректа после успешного удаления
    :return: Рендеринг шаблона с подтверждением удаления
    """
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect(list_url)
    return render(request, 'common_confirm_delete.html', {'obj': obj})

def common_list(request, model, template_name, title, create_url, edit_url, delete_url):
    """
    Универсальная функция для отображения списка объектов модели.

    :param request: Объект запроса
    :param model: Модель для получения списка объектов
    :param template_name: Шаблон для отображения списка
    :param title: Заголовок страницы
    :param create_url: URL для создания нового объекта
    :param edit_url: URL для редактирования объекта
    :param delete_url: URL для удаления объекта
    :return: Рендеринг шаблона с данными
    """
    items = model.objects.all()
    return render(request, template_name, {
        'items': items,
        'title': title,
        'create_url': create_url,
        'edit_url': edit_url,
        'delete_url': delete_url,
    })


# ---- CASHFLOW ----

def cashflow_list(request):
    """ Отображение списка потоков с возможностью фильтрации по различным параметрам."""
    filters = Q()

    if request.GET.get('date_from'):
        filters &= Q(date_created__gte=request.GET['date_from'])
    if request.GET.get('date_to'):
        filters &= Q(date_created__lte=request.GET['date_to'])
    if request.GET.get('status'):
        filters &= Q(status_id=request.GET['status'])
    if request.GET.get('type'):
        filters &= Q(type_id=request.GET['type'])
    if request.GET.get('category'):
        filters &= Q(category_id=request.GET['category'])
    if request.GET.get('subcategory'):
        filters &= Q(subcategory_id=request.GET['subcategory'])

    cashflows = CashFlow.objects.filter(filters)
    statuses = Status.objects.all()
    types = Type.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    context = {
        'cashflows': cashflows,
        'statuses': statuses,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
    }

    return render(request, 'cashflow_list.html', context)


def cashflow_create_or_edit(request, pk=None):
    return common_create_or_edit(request, CashFlow, CashFlowForm, pk, 'Создание/Редактирование потока', 'cashflow_list')

def cashflow_confirm_delete(request, pk):
    return common_confirm_delete(request, CashFlow, pk, 'cashflow_list')


# ---- STATUS ----

def status_list(request):
    return common_list(request, Status, 'common_list.html', 'Статусы', 'status_create', 'status_edit', 'status_delete')

def status_create(request):
    return common_create_or_edit(request, Status, StatusForm, action_title='Создание статуса', list_url='status_list')

def status_edit(request, pk):
    return common_create_or_edit(request, Status, StatusForm, pk, 'Редактирование статуса', 'status_list')

def status_delete(request, pk):
    return common_confirm_delete(request, Status, pk, 'status_list')


# ---- TYPES ----

def type_list(request):
    return common_list(request, Type, 'common_list.html', 'Типы', 'type_create', 'type_edit', 'type_delete')

def type_create(request):
    return common_create_or_edit(request, Type, TypeForm, action_title='Создание типа', list_url='type_list')

def type_edit(request, pk):
    return common_create_or_edit(request, Type, TypeForm, pk, 'Редактирование типа', 'type_list')

def type_confirm_delete(request, pk):
    return common_confirm_delete(request, Type, pk, 'type_list')


# ---- CATEGORIES ----

def category_list(request):
    return common_list(request, Category, 'common_list.html', 'Категории', 'category_create', 'category_edit', 'category_delete')

def category_create(request):
    return common_create_or_edit(request, Category, CategoryForm, action_title='Создание категории', list_url='category_list')

def category_edit(request, pk):
    return common_create_or_edit(request, Category, CategoryForm, pk, 'Редактирование категории', 'category_list')

def category_confirm_delete(request, pk):
    return common_confirm_delete(request, Category, pk, 'cashflow_list')


# ---- SUBCATEGORIES ----

def subcategory_list(request):
    return common_list(request, Subcategory, 'common_list.html', 'Подкатегории', 'subcategory_create', 'subcategory_edit', 'subcategory_delete')

def subcategory_create(request):
    return common_create_or_edit(request, Subcategory, SubcategoryForm, action_title='Создание подкатегории', list_url='subcategory_list')

def subcategory_edit(request, pk):
    return common_create_or_edit(request, Subcategory, SubcategoryForm, pk, 'Редактирование подкатегории', 'subcategory_list')

def subcategory_confirm_delete(request, pk):
    return common_confirm_delete(request, Subcategory, pk, 'subcategory_list')
