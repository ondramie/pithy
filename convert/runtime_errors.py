#!/usr/bin/python3

''' This class captures command errors that were used to determine the 
    accuracy of queries used in elasticsearch database.  There are simple
    errors and more advanced errors that were used for comparison.'''

class StackErrors:
    def __init__(self): 
        # Typical errors 
        self.runtime = "RuntimeError"
        self.value = "ValueError"
        self.zero = "ZeroDivisionError"
        
        self.attrib_error  = "AttributeError: 'str' object has no attribute"
        self.name_error    = "NameError: name 'error' is not defined"
        self.index_error   = "IndexError: list index out of range"
        self.local_error   = "UnboundLocalError: local variable referenced before assignment"

        # This selection of errors were "Dogfood" into elasticsearch errors
        self.es_mlt_small  = "[mlt] query does not support [field]"
        self.es_mlt_medium = """Traceback (most recent call last):
        File "./debugDemyst/upload/querries.py", line 104, in <module>
        main()
        File "./debugDemyst/upload/querries.py", line 80, in main
        s = s.query(MoreLikeThis(like=myError.large_trace_nofolders), fields=['content', 'summary'])
        File "/home/ubuntu/.local/lib/python3.6/site-packages/elasticsearch_dsl/search.py", line 38, in __call__
        proxied._proxied = Q(*args, **kwargs)
        File "/home/ubuntu/.local/lib/python3.6/site-packages/elasticsearch_dsl/query.py", line 23, in Q
        raise ValueError('Q() cannot accept parameters when passing in a Query object.')
        ValueError: Q() cannot accept parameters when passing in a Query object."""

        # This question is from the ubuntu formum; the thread is: 
        # https://askubuntu.com/questions/990013/system-mounts-dev-loop0-on-snap-core-3604-and-its-100-full-where-is-it-comi
        self.mount_q = """/dev/loop0       13M   13M     0 100% /snap/amazon-ssm-agent/495
        /dev/loop1       88M   88M     0 100% /snap/core/5328
        /dev/loop2       88M   88M     0 100% /snap/core/5548
        /dev/loop3       17M   17M     0 100% /snap/amazon-ssm-agent/734"""

        # This is an example of a long stacktrace
        self.long_st = """
        ReferenceError: Input is not defined
            at AdvancedSearchForm.render (~/example.com/views/user/forms/advanced_search.jsx:50:42)
            at ReactCompositeComponentMixin._renderValidatedComponentWithoutOwnerOrContext (~/example.com/node_modules/react/lib/ReactCompositeComponent.js:789:34)
            at ReactCompositeComponentMixin._renderValidatedComponent (~/example.com/node_modules/react/lib/ReactCompositeComponent.js:816:14)
            at wrapper [as _renderValidatedComponent] (~/example.com/node_modules/react/lib/ReactPerf.js:70:21)
            at ReactCompositeComponentMixin.mountComponent (~/example.com/node_modules/react/lib/ReactCompositeComponent.js:237:30)
            at wrapper [as mountComponent] (~/example.com/node_modules/react/lib/ReactPerf.js:70:21)
            at Object.ReactReconciler.mountComponent (~/example.com/node_modules/react/lib/ReactReconciler.js:38:35)
            at ReactDOMComponent.ReactMultiChild.Mixin.mountChildren (~/example.com/node_modules/react/lib/ReactMultiChild.js:192:44)
            at ReactDOMComponent.Mixin._createContentMarkup (~/example.com/node_modules/react/lib/ReactDOMComponent.js:289:32)
            at ReactDOMComponent.Mixin.mountComponent (~/example.com/node_modules/react/lib/ReactDOMComponent.js:199:12)
            at Object.ReactReconciler.mountComponent (~/example.com/node_modules/react/lib/ReactReconciler.js:38:35)
            at ReactCompositeComponentMixin.mountComponent (~/example.com/node_modules/react/lib/ReactCompositeComponent.js:247:34)
            at wrapper [as mountComponent] (~/example.com/node_modules/react/lib/ReactPerf.js:70:21)
            at Object.ReactReconciler.mountComponent (~/example.com/node_modules/react/lib/ReactReconciler.js:38:35)
            at ReactDOMComponent.ReactMultiChild.Mixin.mountChildren (~/example.com/node_modules/react/lib/ReactMultiChild.js:192:44)
            at ReactDOMComponent.Mixin._createContentMarkup (~/example.com/node_modules/react/lib/ReactDOMComponent.js:289:32)
            at ReactDOMComponent.Mixin.mountComponent (~/example.com/node_modules/react/lib/ReactDOMComponent.js:199:12)
            at Object.ReactReconciler.mountComponent (~/example.com/node_modules/react/lib/ReactReconciler.js:38:35)
            at ReactCompositeComponentMixin.mountComponent (~/example.com/node_modules/react/lib/ReactCompositeComponent.js:247:34)
            at wrapper [as mountComponent] (~/example.com/node_modules/react/lib/ReactPerf.js:70:21)
            at Object.ReactReconciler.mountComponent (~/example.com/node_modules/react/lib/ReactReconciler.js:38:35)
            at ReactCompositeComponentMixin.mountComponent (~/example.com/node_modules/react/lib/ReactCompositeComponent.js:247:34)
            at wrapper [as mountComponent] (~/example.com/node_modules/react/lib/ReactPerf.js:70:21)
            at Object.ReactReconciler.mountComponent (~/example.com/node_modules/react/lib/ReactReconciler.js:38:35)
            at ReactDOMComponent.ReactMultiChild.Mixin.mountChildren (~/example.com/node_modules/react/lib/ReactMultiChild.js:192:44)
            at ReactDOMComponent.Mixin._createContentMarkup (~/example.com/node_modules/react/lib/ReactDOMComponent.js:289:32)
            at ReactDOMComponent.Mixin.mountComponent (~/example.com/node_modules/react/lib/ReactDOMComponent.js:199:12)
            at Object.ReactReconciler.mountComponent (~/example.com/node_modules/react/lib/ReactReconciler.js:38:35)
            at ReactCompositeComponentMixin.mountComponent (~/example.com/node_modules/react/lib/ReactCompositeComponent.js:247:34)
            at wrapper [as mountComponent] (~/example.com/node_modules/react/lib/ReactPerf.js:70:21)
            at Object.ReactReconciler.mountComponent (~/example.com/node_modules/react/lib/ReactReconciler.js:38:35)
            at ReactDOMComponent.ReactMultiChild.Mixin.mountChildren (~/example.com/node_modules/react/lib/ReactMultiChild.js:192:44)
            at ReactDOMComponent.Mixin._createContentMarkup (~/example.com/node_modules/react/lib/ReactDOMComponent.js:289:32)
            at ReactDOMComponent.Mixin.mountComponent (~/example.com/node_modules/react/lib/ReactDOMComponent.js:199:12)
            at Object.ReactReconciler.mountComponent (~/example.com/node_modules/react/lib/ReactReconciler.js:38:35)
            at ReactCompositeComponentMixin.mountComponent (~/example.com/node_modules/react/lib/ReactCompositeComponent.js:247:34)
            at wrapper [as mountComponent] (~/example.com/node_modules/react/lib/ReactPerf.js:70:21)
            at Object.ReactReconciler.mountComponent (~/example.com/node_modules/react/lib/ReactReconciler.js:38:35)
            at ReactDOMComponent.ReactMultiChild.Mixin.mountChildren (~/example.com/node_modules/react/lib/ReactMultiChild.js:192:44)
            at ReactDOMComponent.Mixin._createContentMarkup (~/example.com/node_modules/react/lib/ReactDOMComponent.js:289:32)
            at ReactDOMComponent.Mixin.mountComponent (~/example.com/node_modules/react/lib/ReactDOMComponent.js:199:12)
            at Object.ReactReconciler.mountComponent (~/example.com/node_modules/react/lib/ReactReconciler.js:38:35)
            at ReactCompositeComponentMixin.mountComponent (~/example.com/node_modules/react/lib/ReactCompositeComponent.js:247:34)
            at wrapper [as mountComponent] (~/example.com/node_modules/react/lib/ReactPerf.js:70:21)
            at Object.ReactReconciler.mountComponent (~/example.com/node_modules/react/lib/ReactReconciler.js:38:35)
            at ReactCompositeComponentMixin.mountComponent (~/example.com/node_modules/react/lib/ReactCompositeComponent.js:247:34)
            at wrapper [as mountComponent] (~/example.com/node_modules/react/lib/ReactPerf.js:70:21)
            at Object.ReactReconciler.mountComponent (~/example.com/node_modules/react/lib/ReactReconciler.js:38:35)
            at ReactCompositeComponentMixin.mountComponent (~/example.com/node_modules/react/lib/ReactCompositeComponent.js:247:34)
            at wrapper [as mountComponent] (~/example.com/node_modules/react/lib/ReactPerf.js:70:21)
            at ~/example.com/node_modules/react/lib/ReactServerRendering.js:68:32
            at ReactServerRenderingTransaction.Mixin.perform (~/example.com/node_modules/react/lib/Transaction.js:134:20)
            at Object.renderToStaticMarkup (~/example.com/node_modules/react/lib/ReactServerRendering.js:66:24)
            at Object.module.exports [as default] (~/example.com/lib/react-render.js:8:19)
            at Object.<anonymous> (~/example.com/static_routes/render.js:129:49)
            at GeneratorFunctionPrototype.next (native)
        From previous event:
            at Object.<anonymous> (~/example.com/routes/auth.js:72:36)
            at GeneratorFunctionPrototype.next (native)
            at Object.dispatch (~/example.com/node_modules/koa-router/lib/router.js:339:12)
            at GeneratorFunctionPrototype.next (native)
            at onFulfilled (~/example.com/node_modules/bluebird-co/build/yield_handler.js:170:35)
            at ~/example.com/node_modules/bluebird-co/build/yield_handler.js:201:17
            at ~/example.com/node_modules/bluebird-co/build/yield_handler.js:202:15
        From previous event:
            at resolveGenerator (~/example.com/node_modules/bluebird-co/build/yield_handler.js:157:12)
            at toPromise (~/example.com/node_modules/bluebird-co/build/yield_handler.js:218:37)
            at next (~/example.com/node_modules/bluebird-co/build/yield_handler.js:188:47)
        From previous event:
            at Promise.then (~/example.com/node_modules/sequelize/lib/promise.js:21:17)
            at next (~/example.com/node_modules/bluebird-co/build/yield_handler.js:191:42)
            at onFulfilled (~/example.com/node_modules/bluebird-co/build/yield_handler.js:170:25)
            at ~/example.com/node_modules/bluebird-co/build/yield_handler.js:201:17
            at ~/example.com/node_modules/bluebird-co/build/yield_handler.js:202:15
        From previous event:
            at resolveGenerator (~/example.com/node_modules/bluebird-co/build/yield_handler.js:157:12)
            at toPromise (~/example.com/node_modules/bluebird-co/build/yield_handler.js:218:37)
            at next (~/example.com/node_modules/bluebird-co/build/yield_handler.js:188:47)
            at onFulfilled (~/example.com/node_modules/bluebird-co/build/yield_handler.js:170:25)
            at processImmediate [as _immediateCallback] (timers.js:371:17)
        From previous event:
            at Promise.then (~/example.com/node_modules/sequelize/lib/promise.js:21:17)
            at next (~/example.com/node_modules/bluebird-co/build/yield_handler.js:191:42)
            at onFulfilled (~/example.com/node_modules/bluebird-co/build/yield_handler.js:170:25)
            at ~/example.com/node_modules/bluebird-co/build/yield_handler.js:201:17
            at ~/example.com/node_modules/bluebird-co/build/yield_handler.js:202:15
        From previous event:
            at resolveGenerator (~/example.com/node_modules/bluebird-co/build/yield_handler.js:157:12)
            at toPromise (~/example.com/node_modules/bluebird-co/build/yield_handler.js:218:37)
            at ~/example.com/node_modules/bluebird-co/build/yield_handler.js:294:30
        From previous event:
            at Server.<anonymous> (~/example.com/node_modules/koa/lib/application.js:128:8)
            at emitTwo (events.js:87:13)
            at Server.emit (events.js:172:7)
            at HTTPParser.parserOnIncoming [as onIncoming] (_http_server.js:473:12)
            at HTTPParser.parserOnHeadersComplete (_http_common.js:88:23)
            at Socket.socketOnData (_http_server.js:324:22)
            at emitOne (events.js:77:13)
            at Socket.emit (events.js:169:7)
            at readableAddChunk (_stream_readable.js:146:16)
            at Socket.Readable.push (_stream_readable.js:110:10)
            at TCP.onread (net.js:521:20)""" 

        ''' These functions give answers to the errors above.  These were used for testing the 
            accuracy of the queried results.'''
    
    def attrib(self):
        # The question should be https://stackoverflow.com/questions/4005796
        # The answer should be https://stackoverflow.com/a/4005800 
        # The text answer should be:
        """"<p>myList[1] is an element of myList and it's type is string.</p>
        <p>myList[1] is str, you can not append to it.
        myList is a list, you should have been appending to it.</p>
        <pre><code>&gt;&gt;&gt; myList = [1, 'from form', [1,2]]
        &gt;&gt;&gt; myList[1]
        'from form'
        &gt;&gt;&gt; myList[2]
        [1, 2]
        &gt;&gt;&gt; myList[2].append('t')
        &gt;&gt;&gt; myList
        [1, 'from form', [1, 2, 't']]
        &gt;&gt;&gt; myList[1].append('t')
        Traceback (most recent call last):
        File "&lt;stdin&gt;", line 1, in &lt;module&gt;
        AttributeError: 'str' object has no attribute 'append'
        &gt;&gt;&gt; 
        </code></pre>"""
        return 4005800

    def mount_a(self): 
         # the correct answer should be:
        return """That is normal. /dev/loopX are virtual devices to mount image files. And they are -read only- so do not get larger or smaller than they are when created.
        Those mount points are connected to the snapd service. You will see extra loop devices added for every software you install using "snap". Libreoffice has a snap, VLC has one.
        From my system:
        rinzwind@schijfwereld:~$ df -H
        Filesystem      Size  Used Avail Use% Mounted on
        ...
        /dev/loop0       88M   88M     0 100% /snap/core/3440
        /dev/loop2       88M   88M     0 100% /snap/core/3604
        /dev/loop1      204M  204M     0 100% /snap/vlc/65
        /dev/loop3       88M   88M     0 100% /snap/core/3247
        /dev/loop4      121M  121M     0 100% /snap/vlc/4
        I have installed VLC from a snap install so I have 2 extra named "vlc". "core" is used for snapd itself. Remove the service and those loop devices disappear with it (sudo apt purge snapd ubuntu-core-launcher squashfs-tools would remove it; but I would leave it as is if I was you).

        ++++++++++++++++++++++++++ additional info:

        maximum@maxipc:~$ systemctl status snap-core-3604.mount

        snap-core-3604.mount - Mount unit for core
        Loaded: loaded (/etc/systemd/system/snap-core-3604.mount; enabled; vendor pre
        Active: active (mounted) since Wed 2017-12-27 15:44:36 EST; 2min 6s ago
            Where: /snap/core/3604
            What: /dev/loop0
        Process: 838 ExecMount=/bin/mount /var/lib/snapd/snaps/core_3604.snap /snap/co

        Dec 27 15:44:36 maxipc systemd[1]: Mounting Mount unit for core...
        Dec 27 15:44:36 maxipc systemd[1]: Mounted Mount unit for core."""