# -*- generated by 1.0.11 -*-
import da
PatternExpr_469 = da.pat.ConstantPattern('done')
PatternExpr_485 = da.pat.TuplePattern([da.pat.ConstantPattern('client_final_state'), da.pat.FreePattern('client_id'), da.pat.FreePattern('data')])
PatternExpr_508 = da.pat.TuplePattern([da.pat.ConstantPattern('replicas_final_state'), da.pat.FreePattern('data')])
PatternExpr_473 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.ConstantPattern('done')])
_config_object = {'channel': {'fifo', 'reliable'}, 'clock': 'lamport'}
import os
import sys
import logging
import time
import datetime
import uuid
import traceback
da_client = da.import_da('client')
da_replica = da.import_da('replica')
da_olympus = da.import_da('olympus')

class Master(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._MasterReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_0', PatternExpr_469, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_1', PatternExpr_485, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Master_handler_484]), da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_2', PatternExpr_508, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Master_handler_507])])

    def setup(self, config_params, **rest_786):
        super().setup(config_params=config_params, **rest_786)
        self._state.config_params = config_params
        self._state.test_case = self._state.config_params['test_case_name']
        self._state.client_data = {}
        self._state.replica_data = {}
        self._state.num_replicas = ((2 * self._state.config_params['t']) + 1)
        self._state.num_client = self._state.config_params['num_client']
        self._state.logger = self.initialize_logger()
        self._state.logger.info('Master setup completed')

    def run(self):
        start_time = time.time()
        super()._label('_st_label_444', block=False)
        _st_label_444 = 0
        while (_st_label_444 == 0):
            _st_label_444 += 1
            if (len(self._state.client_data) == self._state.num_client):
                _st_label_444 += 1
            else:
                super()._label('_st_label_444', block=True)
                _st_label_444 -= 1
        self.output('All clients done.')
        end_time = time.time()
        self.output('elapsed time (seconds): ', (end_time - start_time))
        self.testcase()
        super()._label('_st_label_466', block=False)
        _st_label_466 = 0
        while (_st_label_466 == 0):
            _st_label_466 += 1
            if PatternExpr_473.match_iter(self._MasterReceivedEvent_0, SELF_ID=self._id):
                _st_label_466 += 1
            else:
                super()._label('_st_label_466', block=True)
                _st_label_466 -= 1

    def initialize_logger(self):
        self._state.logger = logging.getLogger('Master')
        self._state.logger.setLevel(logging.DEBUG)
        path = ('Master-log-' + self._state.test_case)
        fh = logging.FileHandler(path)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self._state.logger.addHandler(fh)
        return self._state.logger

    def testcase(self):
        super()._label('_st_label_311', block=False)
        _st_label_311 = 0
        while (_st_label_311 == 0):
            _st_label_311 += 1
            if (len(self._state.replica_data) == self._state.num_replicas):
                _st_label_311 += 1
            else:
                super()._label('_st_label_311', block=True)
                _st_label_311 -= 1
        self._state.logger.info('comparing all replicas final state of data dictionary')
        for i in range(self._state.num_replicas):
            for j in range((i + 1), self._state.num_replicas):
                replica1 = self._state.replica_data[i]
                replica2 = self._state.replica_data[j]
                length_replica1 = len(replica1)
                length_replica2 = len(replica2)
                if (not (length_replica1 == length_replica2)):
                    self._state.logger.error('replica%s and replica%s final state are different', i, j)
                    self._state.logger.error('test case FAILED')
                    return
                for k in replica1.keys():
                    if (not (replica1[k] == replica2[k])):
                        self._state.logger.error('replica%s & replica%s final state are different', i, j)
                        self._state.logger.error('test case FAILED')
                        return
        self._state.logger.info('all replicas have same final state of data dictionary')
        self._state.logger.info('replicas final state %s ', self._state.replica_data)
        super()._label('_st_label_419', block=False)
        _st_label_419 = 0
        while (_st_label_419 == 0):
            _st_label_419 += 1
            if (len(self._state.client_data) == self._state.num_client):
                _st_label_419 += 1
            else:
                super()._label('_st_label_419', block=True)
                _st_label_419 -= 1
        self._state.logger.info('client final state %s ', self._state.client_data)
        self._state.logger.info('test case PASSED')

    def _Master_handler_484(self, client_id, data):
        self._state.client_data[client_id] = data
        self._state.logger.info('received client%s final state: %s', client_id, data)
    _Master_handler_484._labels = None
    _Master_handler_484._notlabels = None

    def _Master_handler_507(self, data):
        self._state.logger.info('received all replicas final state: %s', data)
        self._state.replica_data = data
    _Master_handler_507._labels = None
    _Master_handler_507._notlabels = None

def read_config(config_file):
    config_params = {}
    with open(config_file, 'r') as f:
        for line in f:
            if (not (line[0] == '#')):
                (key, sep, val) = line.partition('=')
                if (not (len(sep) == 0)):
                    val = val.strip()
                    config_params[key.strip()] = (int(val) if str.isdecimal(val) else val)
    return config_params

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([])

    def run(self):
        config_file = sys.argv[1]

        def build_master(config_params):
            master = self.new(Master, args=(config_params,))
            return master

        def build_olympus(config_params, master):
            olympus = self.new(da_olympus.Olympus, args=(config_params, master), at='OlympusNode')
            return olympus

        def build_client(config_params, olympus, master, client_id):
            client = self.new(da_client.Client, args=(config_params, olympus, master, client_id), at=('ClientNode' + str(client_id)))
            return client
        config_params = read_config(config_file)
        logger = logging.getLogger('Master_logger')
        logger.setLevel(logging.DEBUG)
        path = ('Master-log-' + config_params['test_case_name'])
        fh = logging.FileHandler(path)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.info('building master')
        master = build_master(config_params)
        logger.info('starting master')
        self._start(master)
        logger.info('building olympus')
        olympus = build_olympus(config_params, master)
        logger.info('starting olympus')
        self._start(olympus)
        for client_id in range(config_params['num_client']):
            logger.info('building client : %s', client_id)
            client = build_client(config_params, olympus, master, client_id)
            logger.info('starting client : %s', client_id)
            self._start(client)