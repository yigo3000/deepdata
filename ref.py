def _get_db_create_table(self, frame):

        u"""Returns the MySQL CREATE TABLE statement for the given

        pandas.DataFrame.



        :param frame: pandas.DataFrame.

        :return MySQL CREATE TABLE statement.

        """

        columns = (u',\n'.

                   join([u'  `%s` DECIMAL(20,5) DEFAULT NULL COMMENT "%s"' %

                         (self._get_db_name(name), name) for name in

                         frame.index.values]))

        table_name = self._get_db_table_name(frame)

        return (

            u'CREATE TABLE `%s` (\n' % table_name +

            u'  `ticker` VARCHAR(50) NOT NULL COMMENT "Exchange:Ticker",\n' +

            u'  `period` DATE NOT NULL COMMENT "Period",\n' +

            u'%s,\n' % columns +

            u'  PRIMARY KEY USING BTREE (`ticker`, `period`),\n' +

            u'  KEY `ix_ticker` USING BTREE (`ticker`))\n' +

            u'ENGINE=MyISAM DEFAULT CHARSET=utf8\n' +

            u'COMMENT = "%s"' % frame.index.name)