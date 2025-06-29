# coding: utf-8

"""
    Spartera API Documentation

    Auto-generated API documentation for REST services of the Spartera platform

    The version of the OpenAPI document: 0.0.0
    Contact: support@spartera.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Asset(BaseModel):
    """
    Asset model for every asset (insight/visualization/feed/etc.) customer creates
    """ # noqa: E501
    asset_id: Optional[StrictStr] = None
    user_id: Optional[StrictStr] = None
    company_id: StrictStr
    connection_id: Optional[StrictStr] = None
    llm_connection_id: Optional[StrictStr] = None
    snippet_id: Optional[StrictStr] = None
    industry_id: Optional[StrictStr] = None
    ai_job_id: Optional[StrictStr] = None
    approval_status: Optional[StrictStr] = None
    approved_by_user_id: Optional[StrictStr] = None
    approved_at: Optional[StrictStr] = None
    name: StrictStr
    slug: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    source: StrictStr
    asset_type: Optional[StrictStr] = None
    asset_schema: Optional[StrictStr] = None
    visibility: Optional[StrictStr] = None
    tags: Optional[StrictStr] = None
    sql_logic: Optional[StrictStr] = None
    source_schema_name: Optional[StrictStr] = None
    source_table_name: Optional[StrictStr] = None
    sell_in_marketplace: Optional[StrictStr] = None
    viz_chart_library: Optional[StrictStr] = None
    viz_chart_type: Optional[StrictStr] = None
    viz_dep_var_col_name: Optional[StrictStr] = None
    viz_indep_var_col_name: Optional[StrictStr] = None
    viz_size_col_name: Optional[StrictStr] = None
    viz_color_col_name: Optional[StrictStr] = None
    viz_data_aggregation: Optional[StrictStr] = None
    viz_sort_direction: Optional[StrictStr] = None
    viz_data_limit: Optional[StrictStr] = None
    viz_color_scheme: Optional[StrictStr] = None
    allow_params: Optional[StrictStr] = None
    accept_terms: Optional[StrictStr] = None
    cached: Optional[StrictStr] = None
    schedule: Optional[StrictStr] = None
    next_run: Optional[StrictStr] = None
    data_time_period_start: Optional[StrictStr] = None
    data_time_period_end: Optional[StrictStr] = None
    geographic_coverage_type: Optional[StrictStr] = None
    geographic_coverage_details: Optional[StrictStr] = None
    data_source_refresh_frequency: Optional[StrictStr] = None
    data_source_last_refreshed: Optional[StrictStr] = None
    date_created: Optional[StrictStr] = None
    last_updated: Optional[StrictStr] = None
    active: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["asset_id", "user_id", "company_id", "connection_id", "llm_connection_id", "snippet_id", "industry_id", "ai_job_id", "approval_status", "approved_by_user_id", "approved_at", "name", "slug", "description", "source", "asset_type", "asset_schema", "visibility", "tags", "sql_logic", "source_schema_name", "source_table_name", "sell_in_marketplace", "viz_chart_library", "viz_chart_type", "viz_dep_var_col_name", "viz_indep_var_col_name", "viz_size_col_name", "viz_color_col_name", "viz_data_aggregation", "viz_sort_direction", "viz_data_limit", "viz_color_scheme", "allow_params", "accept_terms", "cached", "schedule", "next_run", "data_time_period_start", "data_time_period_end", "geographic_coverage_type", "geographic_coverage_details", "data_source_refresh_frequency", "data_source_last_refreshed", "date_created", "last_updated", "active"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Asset from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Asset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "asset_id": obj.get("asset_id"),
            "user_id": obj.get("user_id"),
            "company_id": obj.get("company_id"),
            "connection_id": obj.get("connection_id"),
            "llm_connection_id": obj.get("llm_connection_id"),
            "snippet_id": obj.get("snippet_id"),
            "industry_id": obj.get("industry_id"),
            "ai_job_id": obj.get("ai_job_id"),
            "approval_status": obj.get("approval_status"),
            "approved_by_user_id": obj.get("approved_by_user_id"),
            "approved_at": obj.get("approved_at"),
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "description": obj.get("description"),
            "source": obj.get("source"),
            "asset_type": obj.get("asset_type"),
            "asset_schema": obj.get("asset_schema"),
            "visibility": obj.get("visibility"),
            "tags": obj.get("tags"),
            "sql_logic": obj.get("sql_logic"),
            "source_schema_name": obj.get("source_schema_name"),
            "source_table_name": obj.get("source_table_name"),
            "sell_in_marketplace": obj.get("sell_in_marketplace"),
            "viz_chart_library": obj.get("viz_chart_library"),
            "viz_chart_type": obj.get("viz_chart_type"),
            "viz_dep_var_col_name": obj.get("viz_dep_var_col_name"),
            "viz_indep_var_col_name": obj.get("viz_indep_var_col_name"),
            "viz_size_col_name": obj.get("viz_size_col_name"),
            "viz_color_col_name": obj.get("viz_color_col_name"),
            "viz_data_aggregation": obj.get("viz_data_aggregation"),
            "viz_sort_direction": obj.get("viz_sort_direction"),
            "viz_data_limit": obj.get("viz_data_limit"),
            "viz_color_scheme": obj.get("viz_color_scheme"),
            "allow_params": obj.get("allow_params"),
            "accept_terms": obj.get("accept_terms"),
            "cached": obj.get("cached"),
            "schedule": obj.get("schedule"),
            "next_run": obj.get("next_run"),
            "data_time_period_start": obj.get("data_time_period_start"),
            "data_time_period_end": obj.get("data_time_period_end"),
            "geographic_coverage_type": obj.get("geographic_coverage_type"),
            "geographic_coverage_details": obj.get("geographic_coverage_details"),
            "data_source_refresh_frequency": obj.get("data_source_refresh_frequency"),
            "data_source_last_refreshed": obj.get("data_source_last_refreshed"),
            "date_created": obj.get("date_created"),
            "last_updated": obj.get("last_updated"),
            "active": obj.get("active")
        })
        return _obj


