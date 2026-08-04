import { app } from "../../scripts/app.js";

app.registerExtension({

    name: "PromptArchitect.DatasetGenerator",

    async beforeRegisterNodeDef(nodeType, nodeData) {

        if (nodeData.name !== "DatasetGenerator")
            return;

        const onNodeCreated = nodeType.prototype.onNodeCreated;

        nodeType.prototype.onNodeCreated = function () {

            if (onNodeCreated)
                onNodeCreated.apply(this, arguments);

            this.addWidget(
                "button",
                "Scan Builders",
                null,
                () => {

                    console.clear();

                    console.log("========== DATASET ==========");

                    for (const input of this.inputs) {

                        const linkId = input.link;

                        if (linkId == null)
                            continue;

                        const link = this.graph.links[linkId];

                        if (!link)
                            continue;

                        const originNode = this.graph.getNodeById(link.origin_id);

                        console.log(
                            input.name,
                            "->",
                            originNode.type
                        );

                    }

                    console.log("=============================");

                }
            );

        };

    },

});