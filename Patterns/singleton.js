
// singleton pattern example

function Process(state) {
    this.state = state;
}

const Singleton = (function(){
    function ProcessManager() {
        this.numOfProcess = 0;
    }

    let pMan;
    function createProcessManager() {
        pMan = new ProcessManager();
        return pMan;
    }

    return {
        getProcessManager: () => {
            if(!pMan) {
                pMan = createProcessManager();
            }
            return pMan;
        }
    }
})();


const processManager = Singleton.getProcessManager();

const processManager2 = Singleton.getProcessManager();

console.log('singleton check', processManager === processManager2);
