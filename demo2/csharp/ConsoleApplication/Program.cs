using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Salesforce.Common;
using Salesforce.Force;

namespace ConsoleApplication7
{
    class Program
    {
        static void Main(string[] args)
        {
            var task = RunProgram();
            task.Wait();
        }

        private static async Task RunProgram()
        {
            var auth = new AuthenticationClient();

            var clientId = "";
            var clientSecret = "";
            var username = "";
            var password = "";

            await auth.UsernamePasswordAsync(clientId, clientSecret, username, password);

            var client = new ForceClient(auth.InstanceUrl, auth.AccessToken, "v29.0");

            var id = "a06i000000B85NXAAZ";
            var widget = new {Name = "Updated from C#"};

            var success = await client.UpdateAsync("Widget__c", id, widget);

            Console.WriteLine(success);

            if (success)
            {
                var query = "SELECT id, name FROM Widget__c WHERE id = '" + id + "'";
                var response = await client.QueryAsync<dynamic>(query);

                foreach (var result in response.records)
                {
                    Console.WriteLine(result);
                }
            }

        }
    }
}
