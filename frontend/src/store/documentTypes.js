import axios from "axios";

export default {
    actions: {
        async fetchDocumentTypes(ctx) {
            const res = await axios.get('api/document/types/')
            ctx.commit('updateDocumentTypes', res.data)
        }
    },
    mutations: {
        updateDocumentTypes(state, documentTypes) {
            state.documentTypes = documentTypes
        }
    },
    getters: {
        getDocumentTypes(state) {
            const types = []
            for (const i of Object.values(state.documentTypes))
                types.push(i)
            return types
        },
        getDocumentType: state => id => {
            if (id in state.documentTypes)
                return state.documentTypes[id]
            return undefined
        },
        getDocumentId: state => type => {
            for (const [i, tp] of Object.entries(state.documentTypes))
                if (tp === type)
                    return i

            return undefined
        }

        // name: state => attrs => {} - передача атрибутов в getter
    },
    state: {
        documentTypes: {}
    }
}