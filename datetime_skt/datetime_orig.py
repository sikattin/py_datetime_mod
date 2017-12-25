#-------------------------------------------------------------------------------
# Name:        datetime_orig.py
# Purpose:     時間・日付操作用のカスタムモジュール.
#
# Author:      shikano.takeki
#
# Created:     22/12/2017
# Copyright:   (c) shikano.takeki 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
from datetime import datetime
import os


class dateArithmetic(object):
    """日付計算を担当するクラス."""

    def __new__(cls, year=None, month=None, day=None):
        """コンストラクタ"""
        self = object.__new__(cls)
        self._year = year
        self._month = month
        self._day = day
        return self

    def subtract_target_from_now(self, file: str) -> int:
        """現在の日付と対象となるファイルのタイムスタンプの日数差を求める。

        Args:
            param1 file: 対象ファイルのパス.

        Return:
            日数差.
        """
        # 現在の日付.
        now = self.now_datetime()
        # 対象ファイルのタイムスタンプ.
        target_timestmp = datetime.fromtimestamp(os.stat(r"{}".format(file)).st_mtime)
        # 日数差を計算.
        result = now - target_timestmp

        return result.days

    def now_datetime(self):
        """現在の日付を返す

        Returns:
            datetime型のインスタンス.
        """
        return datetime.now()

    def get_year(self):
        """現在の西暦年を返す.

        Returns:
            int型 西暦年
        """
        return datetime.now().year

    def get_month(self):
        """現在の月を返す.

        Returns:
            int型 月
        """
        return datetime.now().month

    def get_day(self):
        """現在の日を返す.

        Returns:
            int型 日
        """
        return datetime.now().day
