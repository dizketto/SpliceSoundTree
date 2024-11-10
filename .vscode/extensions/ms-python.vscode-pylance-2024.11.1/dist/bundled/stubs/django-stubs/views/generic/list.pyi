from collections.abc import Sequence
from typing import Any

from django.core.paginator import Paginator
from django.db.models import Model
from django.db.models.query import QuerySet, _BaseQuerySet
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View

class MultipleObjectMixin(ContextMixin):
    allow_empty: bool = ...
    queryset: QuerySet[Any] | None = ...
    model: type[Model] | None = ...
    paginate_by: int = ...
    paginate_orphans: int = ...
    context_object_name: str | None = ...
    paginator_class: type[Paginator] = ...
    page_kwarg: str = ...
    ordering: Sequence[str] = ...
    def get_queryset(self) -> QuerySet[Any]: ...
    def get_ordering(self) -> Sequence[str]: ...
    def paginate_queryset(
        self, queryset: _BaseQuerySet[Any], page_size: int
    ) -> tuple[Paginator, int, QuerySet[Any], bool]: ...
    def get_paginate_by(self, queryset: _BaseQuerySet[Any]) -> int | None: ...
    def get_paginator(
        self,
        queryset: QuerySet[Any],
        per_page: int,
        orphans: int = ...,
        allow_empty_first_page: bool = ...,
        **kwargs: Any
    ) -> Paginator: ...
    def get_paginate_orphans(self) -> int: ...
    def get_allow_empty(self) -> bool: ...
    def get_context_object_name(
        self, object_list: _BaseQuerySet[Any]
    ) -> str | None: ...

class BaseListView(MultipleObjectMixin, View):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...

class MultipleObjectTemplateResponseMixin(TemplateResponseMixin):
    template_name_suffix: str = ...

class ListView(MultipleObjectTemplateResponseMixin, BaseListView): ...
