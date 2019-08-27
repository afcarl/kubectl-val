from guradctl.model.object.k8s_classes import *

        STATUS_REQ_ATSTART = STATUS_()
        STATUS_REQ_ATLOADBALANCER = STATUS_()
        STATUS_REQ_ATKUBEPROXY = STATUS_()
        STATUS_REQ_ATPODINPUT = STATUS_()
        STATUS_REQ_MEMRESOURCECONSUMED = STATUS_()
        STATUS_REQ_CPURESOURCECONSUMED = STATUS_()
        STATUS_REQ_RESOURCESCONSUMED = STATUS_()
        STATUS_REQ_DIRECTEDTOPOD = STATUS_()
        STATUS_REQ_REQUESTPIDTOBEENDED = STATUS_()
        STATUS_REQ_CPURESOURCERELEASED = STATUS_()
        STATUS_REQ_MEMRESOURCERELEASED = STATUS_()
        STATUS_REQ_RESOURCESRELEASED = STATUS_()
        STATUS_REQ_REQUESTTERMINATED = STATUS_()
        STATUS_REQ_REQUESTFINISHED = STATUS_()
        STATUS_POD_ATCONFIG = STATUS_()
        STATUS_POD_READYTOSTART = STATUS_()
        STATUS_POD_ACTIVE = STATUS_()
        STATUS_POD_PENDING = STATUS_()
        STATUS_POD_ATMANUALCREATION = STATUS_()
        STATUS_POD_DIRECTEDTONODE = STATUS_()
        STATUS_POD_CPUCONSUMED = STATUS_()
        STATUS_POD_RESOURCEFORMALCONSUMPTIONFAILED = STATUS_()
        STATUS_POD_FAILEDTOSTART = STATUS_()
        STATUS_POD_READYTOSTART2 = STATUS_()
        STATUS_POD_MEMCONSUMED = STATUS_()
        STATUS_POD_MEMCONSUMEDFAILED = STATUS_()
        STATUS_POD_BINDEDTONODE = STATUS_()
        STATUS_POD_RUNNING = STATUS_()
        STATUS_POD_SUCCEEDED = STATUS_() # MAY BE LOST BE CAREFUL
        STATUS_POD_KILLING = STATUS_()
        STATUS_POD_FAILED = STATUS_()
        STATUS_NODE_RUNNING = STATUS_()
        STATUS_NODE_SUCCEDED = STATUS_()
        STATUS_POD_PENDING = STATUS_()
        STATUS_NODE_DELETED = STATUS_()
        STATUS_POD_INACTIVE = STATUS_()
        STATUS_NODE_ACTIVE = STATUS_()
        STATUS_NODE_INACTIVE = STATUS_()
        STATUS_REQ_DIRECTEDTONODE = STATUS_()
        STATUS_REQ_NODE_CAPACITYOVERWHELMED = STATUS_()
        STATUS_LIMMET = STATUS_()
        STATUS_LIMOVERWHELMED = STATUS_()
        TEST = STATUS_()
        STATUS_POD_TOBETERMINATED = STATUS_()
        STATUS_POD_TERMINATED = STATUS_()
        STATUS_SERV_PENDING = STATUS_()
        STATUS_SERV_STARTED = STATUS_()
        STATUS_SERV_INTERRUPTED = STATUS_()
        STATUS_REQ_RUNNING = STATUS_()
        STATUS_POD_INITIALCONRELEASED = STATUS_()
        STATUS_POD_GLOBALMEMCONSUMED = STATUS_()
        STATUS_POD_GLOBALCPUCONSUMED = STATUS_()
        STATUS_POD_FORMALCONRELEASED = STATUS_()
        STATUS_SCHED_CLEAN = STATUS_()
        STATUS_SCHED_CHANGED = STATUS_()
        STATUS_POD_READYTOSTART = STATUS_()
        STATUS_POD_FINISHEDPLACEMENT = STATUS_()
        
        STATE_POD_SUCCEEDED = STATE_()
        STATE_POD_RUNNING = STATE_()
        STATE_POD_PENDING = STATE_()
        STATE_POD_ACTIVE = STATE_()
        STATE_POD_INACTIVE = STATE_()
        STATE_REQ_STARTED = STATE_()
        STATE_REQUEST_ACTIVE = STATE_()
        STATE_REQUEST_INACTIVE = STATE_()
        STATE_NODE_ACTIVE = STATE_()
        STATE_NODE_INACTIVE = STATE_()

        
        TYPE_TEMPORARY = Type()
        TYPE_PERSISTENT = Type()
        
        NULL = Type()
        NOTNULL = Type()
        
        ISSUE01 = Type()
        
        PREEMPTLOWERPRIORITY = Type()
        NEVER = Type()
        
        MODEUSERMODE = Mode()
        MODEIPTABLES = MOde()
